import { createHashRouter } from "react-router-dom";
import { DashboardPage } from "@/features/projects/dashboard-page";
import { ConversionPage } from "@/features/inference/conversion-page";
import { ModelsPage } from "@/features/models/models-page";
import { SettingsPage } from "@/features/settings/settings-page";
import { TrainingPage } from "@/features/training/training-page";
import { AppShell } from "@/layouts/app-shell";

export const router = createHashRouter([
  {
    path: "/",
    element: <AppShell />,
    children: [
      {
        index: true,
        element: <DashboardPage />
      },
      {
        path: "models",
        element: <ModelsPage />
      },
      {
        path: "training",
        element: <TrainingPage />
      },
      {
        path: "conversion",
        element: <ConversionPage />
      },
      {
        path: "settings",
        element: <SettingsPage />
      }
    ]
  }
]);
