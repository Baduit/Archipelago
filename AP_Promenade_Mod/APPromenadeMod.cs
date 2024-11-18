using MelonLoader;
using HarmonyLib;
using System;
using System.Reflection;
using Archipelago.MultiClient.Net;
using Archipelago.MultiClient.Net.Enums;
using static DataController;
using System.Collections.Generic;

namespace AP_Promenade
{
    public class APPromenadeMod : MelonMod
    {
        const string gameName = "Pokemon Emerald";
        public static ArchipelagoSession? session = null;
        public static MelonLogger.Instance? logger = null;

        public static int CogCollected = 0;

        [HarmonyPatch(typeof(DataController), "CollectCog", new Type[] { typeof(int), typeof(DataController.Zone) })]
        private static class PatchCollectCog
        {
            private static void Prefix(int _id, DataController.Zone _zone, DataController __instance)
            {
                if (session == null || logger == null)
                    return;

                logger.Msg($"Got cog with id : {_id} in zone {_zone}");

                Type dataControllerType = typeof(DataController);
                FieldInfo dataInfo = dataControllerType.GetField("data", BindingFlags.NonPublic | BindingFlags.Instance);
                FieldInfo cogPiecesHeldInfo = dataControllerType.GetField("cogPiecesHeld", BindingFlags.NonPublic | BindingFlags.Instance);


                int cogPiecesHeld = (int)cogPiecesHeldInfo.GetValue(__instance);
                Dictionary<Zone, WorldInfos> data = (Dictionary<Zone, WorldInfos>)dataInfo.GetValue(__instance);
                cogPiecesHeldInfo.SetValue(__instance, cogPiecesHeld - ((!data[_zone].cogs[_id].isFullCog) ? 1 : 3));

                //long locationId = session.Locations.GetLocationIdFromName(gameName, "Route 103 - Rival Brendan/May");
                Random r = new Random();
                int locationId = r.Next(3860094, 3870386);
                session.Locations.CompleteLocationChecks(locationId);
            }

            private static void Postfix(int _id, DataController.Zone _zone)
            {
            }
        }

        [HarmonyPatch(typeof(DataController), "ComputeCogCollected_Total")]
        private static class PatchComputeCogCollected_Total
        {
            private static bool Prefix(DataController __instance)
            {
                if (session == null || logger == null)
                    return true;

                logger.Msg("ComputeCogCollected_Total called");

                Type dataControllerType = typeof(DataController);
                FieldInfo machineInfosInfo = dataControllerType.GetField("machineInfos", BindingFlags.NonPublic | BindingFlags.Instance);
                FieldInfo cogsHeldInfo = dataControllerType.GetField("cogsHeld", BindingFlags.NonPublic | BindingFlags.Instance);
                FieldInfo cogPiecesHeldInfo = dataControllerType.GetField("cogPiecesHeld", BindingFlags.NonPublic | BindingFlags.Instance);
                FieldInfo cogCollected_TotalInfo = dataControllerType.GetField("cogCollected_Total", BindingFlags.NonPublic | BindingFlags.Instance);

                cogCollected_TotalInfo.SetValue(__instance, CogCollected);

                int cogPiecesHeld = CogCollected;
                MachineCogInfos[] array = (MachineCogInfos[]) machineInfosInfo.GetValue(__instance);
                foreach (MachineCogInfos machineCogInfos in array)
                {
                    cogPiecesHeld -= machineCogInfos.nbCogDelivered * 3;
                }
                cogsHeldInfo.SetValue(__instance, (int)MathF.Floor((float)(cogPiecesHeld / 3)));
                cogPiecesHeldInfo.SetValue(__instance, cogPiecesHeld % 3);
                logger.Msg($"Total Cogs: {CogCollected}, total Cogs piecies Held: {cogPiecesHeld}");

                return false;
            }

            private static void Postfix()
            {
            }
        }

        public override void OnSceneWasLoaded(int buildIndex, string sceneName)
        {
            LoggerInstance.Msg($"Scene {sceneName} with build index {buildIndex} has been loaded!");
        }

        public override void OnLateInitializeMelon()
        {
            string server = "localhost:38281";
            string user = "Emerald";
            LoginResult result;

            try
            {
                session = ArchipelagoSessionFactory.CreateSession(server);
                result = session.TryConnectAndLogin(gameName, user, ItemsHandlingFlags.AllItems, new Version("4.5.0"));
            }
            catch (Exception e)
            {
                result = new LoginFailure(e.GetBaseException().Message);
            }

            if (!result.Successful)
            {
                LoginFailure failure = (LoginFailure)result;
                string errorMessage = $"Failed to Connect to {server} as {user}:";
                foreach (string error in failure.Errors)
                {
                    errorMessage += $"\n    {error}";
                }
                foreach (ConnectionRefusedError error in failure.ErrorCodes)
                {
                    errorMessage += $"\n    {error}";
                }
                LoggerInstance.Error(errorMessage);

                return; // Did not connect, show the user the contents of `errorMessage`
            }

            if (session == null)
                return;

            LoggerInstance.Msg($"Login sucessful to {server}");

            logger = LoggerInstance;

        }
    }

  
}
