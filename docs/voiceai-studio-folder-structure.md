# VoiceAI Studio Folder Structure

## 1. Goal

This structure is designed for a production-grade Windows desktop application built with:

- `Electron`
- `React`
- `Tailwind`
- `Python`
- `SQLite`
- local filesystem storage

It supports these core product areas:

- model downloads
- dataset management
- training
- inference
- audio processing
- download queue
- settings

The layout uses a monorepo so that desktop, frontend, backend, shared contracts, scripts, and docs stay versioned together while remaining cleanly separated.

## 2. Complete Folder Structure

```text
voiceai-studio/
  apps/
    desktop/
      package.json
      electron.vite.config.ts
      tsconfig.json
      tailwind.config.ts
      postcss.config.js
      src/
        main/
          bootstrap/
          config/
          db/
          downloads/
          events/
          ipc/
          jobs/
          logging/
          python/
          security/
          services/
          storage/
          system/
          windows/
          index.ts
        preload/
          api/
          events/
          index.ts
        renderer/
          index.html
          src/
            app/
            assets/
            components/
            features/
              audio/
              datasets/
              downloads/
              inference/
              jobs/
              models/
              projects/
              settings/
              training/
            hooks/
            layouts/
            lib/
            pages/
            routes/
            services/
            store/
            styles/
            types/
            utils/
            main.tsx
  backend/
    pyproject.toml
    requirements.txt
    README.md
    src/
      voiceai_backend/
        __init__.py
        api/
        config/
        core/
        datasets/
        downloads/
        events/
        hardware/
        jobs/
        logging/
        models/
          adapters/
          inspectors/
          registry/
          validators/
        pipelines/
          audio/
          demucs/
          ffmpeg/
          inference/
          training/
        rpc/
        storage/
        utils/
        main.py
    tests/
      unit/
      integration/
      fixtures/
  packages/
    shared/
      package.json
      tsconfig.json
      src/
        constants/
        contracts/
        enums/
        schemas/
        types/
        utils/
    ui/
      package.json
      tsconfig.json
      src/
        audio/
        buttons/
        forms/
        layout/
        feedback/
        index.ts
  resources/
    binaries/
      ffmpeg/
      python/
    icons/
    images/
    model-templates/
    prompts/
  scripts/
    build/
    db/
    dev/
    packaging/
    setup/
    windows/
  docs/
    architecture/
    backend/
    database/
    desktop/
    frontend/
    operations/
    product/
    voiceai-studio-architecture.md
    voiceai-studio-folder-structure.md
    voiceai-studio-prd.md
  config/
    eslint/
    prettier/
    typescript/
  .github/
    workflows/
    ISSUE_TEMPLATE/
    PULL_REQUEST_TEMPLATE.md
  .env.example
  .gitignore
  package.json
  pnpm-workspace.yaml
  README.md
```

## 3. Top-Level Folder Explanations

### `apps/`
Holds deployable applications. In this product there is one desktop app, but this structure leaves room for future tools such as a CLI or diagnostics app.

### `backend/`
Contains the Python AI runtime. This is where all local AI and audio processing logic lives, including training, inference, Demucs separation, FFmpeg workflows, model validation, and worker orchestration.

### `packages/`
Contains shared code reused by multiple apps. This avoids duplicating contracts, schemas, UI primitives, and type definitions across Electron and React.

### `resources/`
Stores packaged static resources and bundled binaries such as `FFmpeg`, icons, model templates, and optionally a managed Python runtime.

### `scripts/`
Contains automation for setup, development, database tasks, packaging, and Windows-specific helper tasks.

### `docs/`
Holds architecture, product, operations, backend, and frontend documentation. This keeps implementation docs close to the codebase.

### `config/`
Contains centralized linting, formatting, and TypeScript configuration shared across the monorepo.

### `.github/`
Stores CI workflows, templates, and repository automation if you host the repo on GitHub.

## 4. Desktop Application Structure

### `apps/desktop/`
Owns the Electron application, React renderer, preload bridge, and desktop packaging configuration.

### `apps/desktop/package.json`
Defines desktop dependencies, scripts, and packaging commands.

### `apps/desktop/electron.vite.config.ts`
Configures the build pipeline for Electron main, preload, and renderer bundles.

### `apps/desktop/tailwind.config.ts`
Defines the Tailwind theme, tokens, and UI styling configuration for the renderer.

### `apps/desktop/src/`
Contains all source code for the desktop application.

## 5. Electron Main Process Folders

### `apps/desktop/src/main/`
Contains the trusted Electron main process. This layer owns orchestration, persistence boundaries, job lifecycle, downloads, filesystem access, and Python supervision.

### `apps/desktop/src/main/bootstrap/`
Startup wiring such as app initialization, service registration, migrations, dependency checks, and first-run boot logic.

### `apps/desktop/src/main/config/`
Loads and validates app configuration such as paths, environment settings, feature flags, and runtime defaults.

### `apps/desktop/src/main/db/`
Owns SQLite setup, migrations, repository classes, queries, and transaction helpers.

### `apps/desktop/src/main/downloads/`
Implements Hugging Face downloads, queue scheduling, pause/resume support, retries, integrity checks, and download persistence.

### `apps/desktop/src/main/events/`
Defines the internal event bus, event publishers, event subscribers, and event-to-renderer fan-out logic.

### `apps/desktop/src/main/ipc/`
Contains all IPC channels, request handlers, input validation, and typed command/query dispatch between renderer and main.

### `apps/desktop/src/main/jobs/`
Owns background job creation, state transitions, cancellation, retries, queue assignment, and coordination with Python workers.

### `apps/desktop/src/main/logging/`
Contains structured logging setup for app logs, job logs, and diagnostic logs.

### `apps/desktop/src/main/python/`
Manages Python backend startup, health checks, worker process supervision, JSON RPC messaging, and restart logic.

### `apps/desktop/src/main/security/`
Holds Electron security configuration such as allowed IPC surfaces, token storage helpers, path validation, and hardened browser window options.

### `apps/desktop/src/main/services/`
Contains business-level services like `ProjectService`, `DatasetService`, `ModelRegistryService`, `SettingsService`, and `ArtifactService`.

### `apps/desktop/src/main/storage/`
Abstracts filesystem ownership for projects, datasets, models, cache, exports, and temp artifacts.

### `apps/desktop/src/main/system/`
Contains machine-level utilities such as OS inspection, disk checks, hardware probes, and app health diagnostics.

### `apps/desktop/src/main/windows/`
Defines BrowserWindow creation, lifecycle handling, splash screens, and desktop window-specific behavior.

### `apps/desktop/src/main/index.ts`
Application entry point for the Electron main process.

## 6. Preload Bridge Folders

### `apps/desktop/src/preload/`
Contains the secure preload layer exposed to the React renderer.

### `apps/desktop/src/preload/api/`
Defines whitelisted APIs such as projects, downloads, jobs, training, inference, settings, and system accessors.

### `apps/desktop/src/preload/events/`
Handles renderer subscriptions for job progress, download updates, logs, and system notifications.

### `apps/desktop/src/preload/index.ts`
Exports the `window.voiceai` bridge and registers secure IPC wrappers.

## 7. React Renderer Folders

### `apps/desktop/src/renderer/`
Contains the React application rendered inside Electron.

### `apps/desktop/src/renderer/src/app/`
Top-level app wiring such as providers, bootstrapping, app shell, theme setup, and global state hydration.

### `apps/desktop/src/renderer/src/assets/`
Static frontend assets such as logos, local illustrations, and UI-only media files.

### `apps/desktop/src/renderer/src/components/`
Shared React components used across multiple features, such as dialogs, tables, cards, form controls, and progress indicators.

### `apps/desktop/src/renderer/src/features/`
Feature-sliced application modules grouped by business domain.

### `apps/desktop/src/renderer/src/features/audio/`
Waveform viewers, audio players, scrubbing tools, preview controls, and merge/export UI.

### `apps/desktop/src/renderer/src/features/datasets/`
Dataset list pages, import flows, clip review, quality indicators, tagging, and dataset readiness UI.

### `apps/desktop/src/renderer/src/features/downloads/`
Download center, model download UI, queue visualization, progress bars, and retry/pause controls.

### `apps/desktop/src/renderer/src/features/inference/`
Voice conversion flows, inference settings, model selection, preview generation, and output review screens.

### `apps/desktop/src/renderer/src/features/jobs/`
Job center, logs, queue state, job details, cancellation controls, and failure recovery flows.

### `apps/desktop/src/renderer/src/features/models/`
Model registry views, model details, validation status, compatibility indicators, and local model management.

### `apps/desktop/src/renderer/src/features/projects/`
Project creation, dashboard, project switching, file organization, and artifact overview screens.

### `apps/desktop/src/renderer/src/features/settings/`
User preferences for directories, GPU behavior, Hugging Face token, export defaults, cache, and diagnostics.

### `apps/desktop/src/renderer/src/features/training/`
Training setup forms, parameter controls, dataset selection, training progress, checkpoints, and trained model registration flows.

### `apps/desktop/src/renderer/src/hooks/`
Custom React hooks such as subscription hooks, keyboard shortcuts, audio controls, and IPC wrappers.

### `apps/desktop/src/renderer/src/layouts/`
Reusable application layouts like the main workspace shell, settings shell, and job detail layout.

### `apps/desktop/src/renderer/src/lib/`
Renderer-only infrastructure helpers such as schema helpers, formatters, audio math utilities, and feature helpers.

### `apps/desktop/src/renderer/src/pages/`
Page-level route components, typically composed from feature modules.

### `apps/desktop/src/renderer/src/routes/`
Router definitions, route guards, lazy loading configuration, and navigation mapping.

### `apps/desktop/src/renderer/src/services/`
Frontend service wrappers for preload APIs, query caching, and renderer-side orchestration helpers.

### `apps/desktop/src/renderer/src/store/`
Global state stores for UI state, project state, current jobs, downloads, and preferences.

### `apps/desktop/src/renderer/src/styles/`
Tailwind entry files, global CSS, theme tokens, typography, and utility layers.

### `apps/desktop/src/renderer/src/types/`
Renderer-local TypeScript types that do not belong in shared contracts.

### `apps/desktop/src/renderer/src/utils/`
General helpers such as date formatting, byte conversions, validation helpers, and file display utilities.

### `apps/desktop/src/renderer/src/main.tsx`
React application entry point.

## 8. Python Backend Folders

### `backend/src/voiceai_backend/`
Main Python package for AI, media, job, and storage logic.

### `backend/src/voiceai_backend/api/`
Optional internal application service layer for backend commands if you want a command-oriented module boundary above raw pipelines.

### `backend/src/voiceai_backend/config/`
Python-side configuration loading for paths, worker limits, model defaults, and runtime environment flags.

### `backend/src/voiceai_backend/core/`
Shared backend primitives such as base service classes, exceptions, result objects, and dependency wiring.

### `backend/src/voiceai_backend/datasets/`
Dataset import, normalization, metadata extraction, clip validation, and training dataset preparation.

### `backend/src/voiceai_backend/downloads/`
Backend-side helpers for download validation or model inspection if Python participates in post-download checks.

### `backend/src/voiceai_backend/events/`
Progress emitters, event envelope builders, log routing, and job signal helpers for the Python runtime.

### `backend/src/voiceai_backend/hardware/`
GPU, CUDA, VRAM, CPU, and memory detection logic used for capability checks and runtime recommendations.

### `backend/src/voiceai_backend/jobs/`
Worker scheduling, cancellation tokens, execution context, queue adapters, and job lifecycle helpers.

### `backend/src/voiceai_backend/logging/`
Structured logging setup for pipeline logs, worker logs, and diagnostics.

### `backend/src/voiceai_backend/models/`
Model management code for local model files, metadata inspection, validation, and compatibility logic.

### `backend/src/voiceai_backend/models/adapters/`
Tool-specific adapters for `RVC`, `Demucs`, and any future model family.

### `backend/src/voiceai_backend/models/inspectors/`
Logic for reading local model files, configs, index files, and metadata to determine compatibility and readiness.

### `backend/src/voiceai_backend/models/registry/`
Backend-side model registration helpers and model discovery logic.

### `backend/src/voiceai_backend/models/validators/`
Validation rules for file structure, config expectations, supported formats, and pipeline compatibility.

### `backend/src/voiceai_backend/pipelines/`
Contains the actual processing workflows.

### `backend/src/voiceai_backend/pipelines/audio/`
Shared audio preprocessing tasks like trimming, normalization, resampling, and channel conversion.

### `backend/src/voiceai_backend/pipelines/demucs/`
Demucs-based separation workflows and related artifact production.

### `backend/src/voiceai_backend/pipelines/ffmpeg/`
FFmpeg wrappers for merge, encode, mux, and export operations.

### `backend/src/voiceai_backend/pipelines/inference/`
RVC inference and voice conversion workflows.

### `backend/src/voiceai_backend/pipelines/training/`
RVC training, feature extraction, checkpointing, and trained model artifact generation.

### `backend/src/voiceai_backend/rpc/`
Defines the JSON RPC server, request parsing, response encoding, and contract dispatch between Electron and Python.

### `backend/src/voiceai_backend/storage/`
Python-side file access helpers for temporary work directories, artifact staging, and output manifests.

### `backend/src/voiceai_backend/utils/`
Small shared utilities used across backend modules.

### `backend/src/voiceai_backend/main.py`
Python process entry point.

## 9. Backend Test Folders

### `backend/tests/unit/`
Fast isolated tests for helpers, validators, job logic, and metadata parsing.

### `backend/tests/integration/`
Tests that exercise real pipelines or multi-module flows such as model inspection, FFmpeg calls, or RPC behavior.

### `backend/tests/fixtures/`
Small sample files, fake metadata, and test artifacts used by backend tests.

## 10. Shared Package Folders

### `packages/shared/`
Contains contracts used across Electron main, preload, and renderer.

### `packages/shared/src/constants/`
Global constants such as channel names, queue names, status enums, and path keys.

### `packages/shared/src/contracts/`
Core IPC and RPC contract definitions for commands, queries, events, and payload shapes.

### `packages/shared/src/enums/`
Shared enums for job statuses, model families, artifact types, and download states.

### `packages/shared/src/schemas/`
`zod` schemas for validation of request payloads, responses, settings, and event envelopes.

### `packages/shared/src/types/`
Cross-process TypeScript types shared across app layers.

### `packages/shared/src/utils/`
Pure shared helpers that are safe to use in any TypeScript runtime.

### `packages/ui/`
Optional shared UI component package for React primitives used across pages and features.

### `packages/ui/src/audio/`
Reusable waveform and audio interaction UI pieces.

### `packages/ui/src/buttons/`
Standardized button components and variants.

### `packages/ui/src/forms/`
Reusable form inputs, field wrappers, sliders, switches, and validation UI.

### `packages/ui/src/layout/`
Page shells, panels, stacks, and container primitives.

### `packages/ui/src/feedback/`
Progress bars, toasts, alerts, empty states, and skeleton components.

## 11. Resources Folder

### `resources/`
Bundles non-source runtime assets.

### `resources/binaries/`
Contains packaged binaries used by the app at runtime.

### `resources/binaries/ffmpeg/`
Holds the Windows `FFmpeg` binary and related executables if bundled.

### `resources/binaries/python/`
Optional embedded Python runtime or bootstrap assets for managing the backend runtime.

### `resources/icons/`
Application icons for Electron packaging and installer assets.

### `resources/images/`
Static imagery used in onboarding, empty states, or product branding.

### `resources/model-templates/`
Starter templates, model manifests, or compatibility templates for supported local model types.

### `resources/prompts/`
Optional prompt/config templates for guided setup or diagnostics flows.

## 12. Scripts Folder

### `scripts/build/`
Build scripts for monorepo production builds, asset preparation, and release packaging.

### `scripts/db/`
Database generation, migrations, seeding, inspection, and maintenance utilities.

### `scripts/dev/`
Developer commands to start Electron, React, and Python together in local development.

### `scripts/packaging/`
Installer creation, binary embedding, release artifact preparation, and signing helpers.

### `scripts/setup/`
Bootstrap scripts for dependencies, environment checks, and first-time developer setup.

### `scripts/windows/`
Windows-specific helpers such as path setup, PowerShell wrappers, and platform diagnostics.

## 13. Docs Folder

### `docs/architecture/`
Detailed system design documents, process diagrams, IPC flow specs, and module boundaries.

### `docs/backend/`
Python backend internals, pipeline docs, worker model details, and model integration notes.

### `docs/database/`
SQLite schema docs, migration rules, and query design notes.

### `docs/desktop/`
Electron main, preload, packaging, and runtime behavior documentation.

### `docs/frontend/`
React app architecture, component conventions, route organization, and state management guidance.

### `docs/operations/`
Build, packaging, release, installer, crash recovery, and support playbooks.

### `docs/product/`
PRD, roadmap, UX flows, feature specs, and release scope documents.

## 14. Config Folder

### `config/eslint/`
Shared lint rules across desktop and packages.

### `config/prettier/`
Central formatting configuration.

### `config/typescript/`
Shared base TypeScript configs for the monorepo.

## 15. Recommended Local Runtime Data Layout

This is not source-controlled, but the application should create and manage a local user data tree like this:

```text
%APPDATA%/VoiceAIStudio/
  config/
  db/
  logs/
  cache/
  downloads/
  temp/
  models/
    huggingface/
    trained/
  datasets/
  projects/
    <project-id>/
      inputs/
      stems/
      inference/
      exports/
      checkpoints/
      metadata/
```

### `config/`
Stores resolved user settings and local app configuration.

### `db/`
Stores the `SQLite` database file and migration state.

### `logs/`
Stores app, job, backend, and crash logs.

### `cache/`
Stores reusable cache artifacts such as temporary processed files and intermediate model data.

### `downloads/`
Stores partial and completed downloads before registration or movement.

### `temp/`
Stores disposable working files for currently running tasks.

### `models/`
Stores downloaded and trained voice models.

### `datasets/`
Stores managed datasets and imported clips.

### `projects/`
Stores project-specific media, outputs, and metadata.

## 16. Why This Structure Works

- It separates trusted desktop orchestration from untrusted UI rendering.
- It gives Python a clean backend boundary for AI and media pipelines.
- It makes job systems, downloads, training, and inference first-class modules.
- It prevents feature code from spreading randomly across the repo.
- It supports scaling from MVP to production without major structural rewrites.
- It keeps shared contracts centralized, which is critical for IPC-heavy desktop apps.

## 17. Recommended Ownership Rules

- `Electron Main` owns orchestration, persistence, queues, job state, and secure system access.
- `React Renderer` owns presentation, user interaction, and transient UI state.
- `Python Backend` owns AI execution, audio processing, and hardware-aware compute logic.
- `packages/shared` owns schemas and contracts used across boundaries.
- `SQLite` stores metadata only; large binaries stay in the local filesystem.

## 18. Final Recommendation

This structure is strong enough for a production VoiceAI Studio codebase and still practical for an MVP. It keeps `Electron`, `React`, and `Python` sharply separated, while giving downloads, datasets, training, inference, audio processing, settings, and background jobs their own clear homes.
