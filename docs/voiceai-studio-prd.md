# VoiceAI Studio Product Requirements Document

## 1. Product Overview

### 1.1 Product Name
`VoiceAI Studio`

### 1.2 Product Summary
VoiceAI Studio is a Windows desktop application for local-first AI voice workflows. It enables users to upload songs, manage voice datasets, download supported models from Hugging Face, train voice models, perform vocal separation, convert vocals, merge audio, and organize local projects entirely on their own machine.

The product is designed around privacy, ownership, and offline-capable processing. All inference, training, conversion, dataset management, and file storage happen locally. No cloud inference or server-side processing is used.

### 1.3 Vision
Create a professional-grade local voice AI workstation for creators who want complete control over their data, models, and outputs without relying on remote services.

### 1.4 Objectives
- Enable fully local voice AI workflows on Windows.
- Provide an approachable UI for technically complex audio and model operations.
- Support local model download, storage, training, and inference.
- Use available GPU resources automatically when supported.
- Keep all audio assets, datasets, models, job outputs, and project state locally organized.

### 1.5 Non-Goals
- Cloud-based inference
- Server-side project storage
- Browser-only access
- Real-time collaboration features
- Online model marketplace beyond direct Hugging Face downloads
- macOS or Linux support in the initial release

## 2. Target Users

### 2.1 Primary Users
- Independent music creators
- Voice conversion hobbyists
- AI audio experimenters
- Small audio studios
- Technical creators building custom local voice models

### 2.2 User Needs
- Convert songs into a target voice locally
- Organize and curate datasets for training
- Train voice models using local compute
- Download compatible models from Hugging Face
- Separate vocals and instrumentals for preprocessing and remixing
- Manage projects, outputs, and model files cleanly on disk

## 3. Product Scope

### 3.1 Core Requirements
- Electron desktop application
- React frontend
- Python AI backend
- All processing happens locally on the user's computer
- No cloud inference
- No server-side processing
- Models are downloaded directly from Hugging Face
- Models are stored locally
- Voice datasets are stored locally
- Voice training happens locally
- Song conversion happens locally

### 3.2 Core Features
1. Song Upload
2. Voice Dataset Manager
3. Voice Model Training
4. Hugging Face Model Downloader
5. Vocal Separation
6. Voice Conversion
7. Audio Merging
8. Local Project Management
9. GPU Detection
10. Download Manager

## 4. Product Goals and Success Metrics

### 4.1 Business and Product Goals
- Reduce the setup friction for local AI voice workflows
- Offer a trusted privacy-first alternative to cloud AI audio tools
- Provide one integrated application instead of multiple disconnected scripts

### 4.2 Success Metrics
- User completes first project creation successfully
- User completes first model download successfully
- User completes first conversion successfully
- User completes first dataset import successfully
- User completes first training workflow successfully
- Time to first successful conversion is under 15 minutes after dependencies are ready
- Long-running job failure rate remains low and errors are recoverable

## 5. Assumptions and Constraints

### 5.1 Assumptions
- Users are on Windows 10 or Windows 11 64-bit systems
- Users may have either CPU-only or GPU-capable machines
- Users are willing to download large model files locally
- Users may need guided setup for Python/runtime dependencies

### 5.2 Constraints
- No remote inference or training
- No backend web service
- Must tolerate large file sizes and long-running operations
- Must support direct Hugging Face model download workflows
- Must remain usable with intermittent or no internet after setup

## 6. User Flows

### 6.1 First-Time Setup Flow
1. User installs and launches VoiceAI Studio.
2. Application verifies local prerequisites and initializes the Python backend.
3. Application detects available CPU/GPU resources.
4. User selects local storage directories for projects, models, datasets, cache, and outputs.
5. Application recommends required or optional starter models.
6. User downloads selected models from Hugging Face.
7. User lands on the dashboard and can begin a project.

### 6.2 Song Upload and Conversion Flow
1. User creates a new project or opens an existing project.
2. User uploads a source song.
3. Application validates the file format, metadata, and readability.
4. User optionally runs vocal separation.
5. User selects a target voice model.
6. User adjusts inference settings such as pitch, blend, or protection parameters.
7. User starts a conversion job.
8. Application displays progress, logs, and job state.
9. User previews converted vocals.
10. User merges converted vocals with the instrumental if needed.
11. User exports the final output locally.

### 6.3 Dataset Management Flow
1. User opens Dataset Manager.
2. User creates a new dataset.
3. User imports one or more audio files or folders.
4. Application validates audio structure and extracts metadata.
5. User previews clips, removes low-quality clips, and tags content.
6. Application stores dataset files and metadata locally.
7. User links the dataset to a training workflow.

### 6.4 Model Training Flow
1. User opens a prepared dataset.
2. User starts a new training session.
3. Application validates dataset quality and system requirements.
4. User selects training parameters.
5. Application estimates training time, disk usage, and hardware feasibility.
6. User starts training.
7. Python backend executes local training.
8. Application streams logs, checkpoints, progress, and warnings.
9. User stops, resumes, or restarts if supported by the training pipeline.
10. Trained model is saved into the local model registry.

### 6.5 Hugging Face Model Download Flow
1. User opens Model Downloader.
2. User searches for a model or pastes a Hugging Face repository URL.
3. Application displays metadata such as model size, files, license, and compatibility.
4. User selects a local destination.
5. Download Manager fetches files directly from Hugging Face.
6. Application verifies file integrity where possible.
7. Downloaded model is registered for local use.

### 6.6 Project Management Flow
1. User creates a project with a name and storage path.
2. Application creates the project folder structure locally.
3. User adds songs, datasets, models, and output artifacts to the project.
4. Application saves metadata and job history locally.
5. User reopens the project later and continues work.

## 7. Functional Requirements

### 7.1 Desktop Application Shell
- The system shall run as a Windows desktop application using Electron.
- The UI shall be implemented in React with TypeScript.
- The Electron main process shall manage lifecycle, windowing, filesystem access, IPC, downloads, and backend orchestration.
- The renderer shall not access Node APIs directly.
- The preload layer shall expose only whitelisted APIs to the renderer.

### 7.2 Python AI Backend
- The system shall run a local Python backend as a child process or managed worker process.
- The backend shall perform all AI-related tasks locally, including preprocessing, separation, training, and conversion.
- The backend shall communicate progress, logs, and job state back to Electron using structured local messaging.
- The backend shall not depend on cloud services for inference or training.

### 7.3 Song Upload
- Users shall be able to upload local audio files in supported formats including `wav`, `mp3`, `flac`, and `ogg`.
- The system shall validate file type, readability, duration, sample rate, and corruption.
- Uploaded songs shall be copied or linked into a local project workspace.
- The UI shall display basic metadata and waveform preview.

### 7.4 Voice Dataset Manager
- Users shall be able to create, rename, archive, and delete datasets.
- Users shall be able to import datasets from files or folders.
- Users shall be able to preview clips before training.
- Users shall be able to remove invalid or low-quality clips.
- Users shall be able to tag datasets and clips with metadata.
- The system shall store dataset metadata locally.
- The system shall validate minimum quality thresholds before training starts.

### 7.5 Voice Model Training
- Users shall be able to start local training jobs from selected datasets.
- Users shall be able to configure training parameters such as epochs, batch size, learning rate, and checkpoint intervals.
- The system shall estimate expected resource usage and warn users when requirements exceed available resources.
- The system shall display progress, status, ETA, logs, and checkpoints.
- The system shall support interruption handling and resume behavior where supported by the model pipeline.
- Trained models shall be stored locally and registered in the model catalog.

### 7.6 Hugging Face Model Downloader
- Users shall be able to search for supported models or paste a direct Hugging Face model URL.
- The system shall download model files directly from Hugging Face to local storage.
- The system shall support authenticated downloads using a locally stored Hugging Face token for gated models.
- The system shall show download size, progress, speed, status, and completion state.
- The system shall verify file integrity where checksums or metadata are available.
- Downloaded models shall be indexed and made available in model selection UIs.

### 7.7 Vocal Separation
- Users shall be able to run local vocal separation on uploaded songs.
- The system shall support at minimum two outputs: vocal stem and instrumental stem.
- Separation outputs shall be stored within the local project workspace.
- Users shall be able to preview separated outputs before proceeding.

### 7.8 Voice Conversion
- Users shall be able to choose an input vocal track and a target voice model.
- Users shall be able to adjust conversion settings supported by the selected model family.
- The system shall perform conversion locally and asynchronously.
- The system shall provide progress feedback and detailed failure reporting.
- The system shall save converted outputs into the project output structure.

### 7.9 Audio Merging
- Users shall be able to merge converted vocals with an instrumental track.
- Users shall be able to adjust vocal gain, instrumental gain, fade in, fade out, and alignment.
- Users shall be able to export merged audio in supported formats such as `wav` and `mp3`.

### 7.10 Local Project Management
- Users shall be able to create, open, rename, duplicate, archive, and delete projects.
- Projects shall maintain local metadata for files, jobs, models used, outputs, and settings.
- Users shall be able to reopen previous projects and continue work without re-importing assets.

### 7.11 GPU Detection
- The system shall detect local GPU availability during startup and on demand.
- The system shall detect CUDA compatibility, VRAM capacity, and fallback mode where feasible.
- The system shall surface clear guidance if the machine is CPU-only or insufficient for a selected workload.

### 7.12 Download Manager
- The system shall manage long-running file downloads independently from the active screen.
- Users shall be able to pause, resume, cancel, retry, and inspect downloads.
- The system shall preserve interrupted download state when possible.

### 7.13 Job Management
- The system shall track all long-running jobs including downloads, separation, training, conversion, and export.
- Each job shall have a unique identifier, type, status, progress, timestamps, logs, and related artifacts.
- Job progress shall remain visible even when the user navigates away from the originating page.

### 7.14 Settings and Local Configuration
- Users shall be able to configure storage directories, cache size, temporary directories, output formats, backend paths, and hardware preferences.
- Users shall be able to add or update a Hugging Face access token.
- Users shall be able to clear cache and temporary job artifacts.

## 8. Non-Functional Requirements

### 8.1 Privacy
- No user audio, datasets, models, metadata, or outputs shall be sent to any application-owned server.
- Internet connectivity shall only be required for direct user-initiated external downloads such as Hugging Face assets and optional dependency setup.

### 8.2 Security
- The renderer process shall be isolated using Electron security best practices.
- Node integration shall be disabled in the renderer.
- The preload layer shall expose a restricted API surface.
- All IPC payloads shall be validated.
- Local tokens shall be stored securely using OS-protected secure storage where possible.
- Downloaded files shall never be executed as arbitrary code.

### 8.3 Performance
- Standard UI navigation actions should respond within 200 milliseconds under normal conditions.
- Heavy operations shall run asynchronously without blocking the UI.
- The system should leverage GPU acceleration automatically when available and compatible.

### 8.4 Reliability
- The system shall recover gracefully from backend process crashes where possible.
- Interrupted downloads should resume when supported by the source and local state.
- Project metadata should survive unexpected app restarts.
- Long-running jobs shall produce persistent logs for diagnostics.

### 8.5 Scalability on Device
- The system shall support large datasets, model files, and output artifacts without storing them as database blobs.
- Metadata indexing shall remain performant for large local libraries.

### 8.6 Usability
- The system shall support a guided first-run experience.
- Errors shall be actionable and understandable to non-expert users.
- Major workflows shall be accessible without requiring command-line interaction.

### 8.7 Maintainability
- The architecture shall separate UI concerns, desktop orchestration, backend computation, and storage responsibilities.
- Shared contracts between Electron and Python-facing layers shall be strongly typed where practical.
- New pipelines and model families should be pluggable through adapters.

### 8.8 Compatibility
- Initial release target: Windows 10 and Windows 11, 64-bit only.
- The system should support offline usage after setup and model download.

### 8.9 Observability
- The system shall maintain structured local logs for app events, downloads, jobs, and backend processes.
- Users shall be able to inspect job-level logs and error details within the UI.

## 9. Technical Architecture

### 9.1 Architecture Style
VoiceAI Studio should use a modular local desktop architecture composed of four layers:

1. Electron Main Process
2. Electron Preload IPC Bridge
3. React Renderer
4. Python AI Backend

### 9.2 High-Level Component Responsibilities

#### Electron Main Process
- Application lifecycle and startup
- Window creation and management
- Secure IPC routing
- Filesystem orchestration
- Download management
- Job scheduling and lifecycle tracking
- Python backend process supervision
- Local database access orchestration

#### Electron Preload Layer
- Secure API bridge between renderer and main process
- Typed IPC client wrappers
- Event subscriptions for job progress, downloads, and state changes

#### React Renderer
- Dashboard and navigation
- Project management screens
- Dataset management screens
- Model downloader and registry views
- Conversion, separation, and training workflow screens
- Download center
- Job monitor
- Settings and onboarding

#### Python AI Backend
- Audio preprocessing
- Vocal separation pipelines
- Voice conversion pipelines
- Voice model training pipelines
- Hardware capability detection
- Model loading and validation
- Job execution workers
- Structured progress and log events

### 9.3 Communication Pattern
- React communicates with Electron through preload-exposed APIs only.
- Electron communicates with the Python backend using local inter-process communication.
- Preferred V1 communication model: `stdin/stdout` JSON RPC or newline-delimited JSON messaging.
- Alternative local-only option: a `127.0.0.1` loopback service, if streaming and worker management require it.

### 9.4 Suggested Technology Stack
- Desktop shell: `Electron`
- Frontend: `React` + `TypeScript`
- State management: `Zustand` or `Redux Toolkit`
- Styling: `Tailwind CSS` or `CSS Modules`
- Audio waveform/preview: `wavesurfer.js`
- Backend runtime: `Python 3.11+`
- ML/audio libraries: `PyTorch`, `torchaudio`, `librosa`, `soundfile`, `ffmpeg`
- Hugging Face integration: `huggingface_hub`
- Local metadata store: `SQLite`
- Validation: `zod` for Electron/renderer contracts
- Packaging: `electron-builder`

### 9.5 Recommended Internal Services
- `ProjectService`
- `DatasetService`
- `ModelRegistryService`
- `DownloadService`
- `JobService`
- `SettingsService`
- `HardwareDetectionService`
- `AudioProcessingService`
- `SeparationService`
- `TrainingService`
- `ConversionService`

### 9.6 Data Storage Strategy

#### Structured Metadata
Use `SQLite` for:
- projects
- datasets
- models
- downloads
- jobs
- outputs
- application settings

#### Large Binary Assets
Use the filesystem for:
- source songs
- separated stems
- converted vocals
- merged outputs
- model weights
- training checkpoints
- cached downloads
- datasets
- temporary processing artifacts

Store file paths in the database rather than storing media as blobs.

### 9.7 Security Architecture
- Enable `contextIsolation: true`
- Disable `nodeIntegration` in renderer windows
- Validate all user-input file paths and IPC payloads
- Restrict preload APIs to explicit commands and events
- Protect Hugging Face tokens using platform-secure credential storage when available
- Prevent arbitrary command execution from user-provided or downloaded assets

### 9.8 Job Execution Model
- Every long-running action should be represented as a tracked job record.
- Job record fields should include:
  - job ID
  - project ID
  - job type
  - status
  - progress percentage
  - start time
  - end time
  - logs
  - output artifact references
  - error information
- Jobs should continue independently of active page navigation.
- Electron should supervise job lifecycle while Python workers execute computational tasks.

### 9.9 Model Pipeline Strategy
Use adapter-based abstractions so the application is not tightly coupled to a single model family.

Recommended adapter families:
- `SeparationAdapter`
- `TrainingAdapter`
- `ConversionAdapter`
- `ModelMetadataAdapter`

This allows future support for multiple compatible local model ecosystems without rewriting the UI contract.

## 10. Data Model Overview

### 10.1 Project
- `id`
- `name`
- `rootPath`
- `createdAt`
- `updatedAt`
- `defaultSettings`

### 10.2 Dataset
- `id`
- `projectId`
- `name`
- `path`
- `clipCount`
- `durationSeconds`
- `sampleRate`
- `status`

### 10.3 Model
- `id`
- `name`
- `source`
- `sourceUrl`
- `localPath`
- `modelType`
- `version`
- `license`
- `compatibility`

### 10.4 Job
- `id`
- `projectId`
- `jobType`
- `status`
- `progress`
- `startedAt`
- `completedAt`
- `logPath`
- `errorMessage`

## 11. Recommended Folder Structure

```text
voiceai-studio/
  apps/
    desktop/
      package.json
      electron.vite.config.ts
      src/
        main/
          bootstrap/
          downloads/
          ipc/
          jobs/
          security/
          services/
          storage/
          windows/
          index.ts
        preload/
          api/
          index.ts
        renderer/
          index.html
          src/
            app/
            components/
            features/
              conversion/
              datasets/
              downloads/
              jobs/
              models/
              projects/
              separation/
              settings/
              training/
            hooks/
            pages/
            services/
            store/
            styles/
            types/
            utils/
  backend/
    pyproject.toml
    requirements.txt
    src/
      voiceai_backend/
        audio/
        config/
        core/
        datasets/
        hardware/
        jobs/
        logging/
        models/
          adapters/
          registry/
          validation/
        pipelines/
          conversion/
          preprocessing/
          separation/
          training/
        storage/
        utils/
        main.py
  packages/
    shared/
      src/
        constants/
        contracts/
        schemas/
        types/
  resources/
    ffmpeg/
    icons/
    templates/
  scripts/
    build/
    dev/
    setup/
  docs/
    architecture/
    prd/
  data/
    sample-projects/
  package.json
  pnpm-workspace.yaml
  README.md
```

## 12. Recommended Local User Data Layout

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
      separated/
      converted/
      merged/
      exports/
      metadata/
      checkpoints/
```

## 13. MVP Scope

### 13.1 MVP Features
- Song upload
- Local project management
- Hugging Face model download
- GPU detection
- Vocal separation
- Basic dataset management
- Basic voice conversion
- Audio merge and export
- Job tracking and logs

### 13.2 Deferred to Phase 2
- Full advanced training workflow
- Dataset quality scoring and automated cleanup suggestions
- Model compatibility scoring
- Batch job pipelines
- Presets and reusable workflow templates
- Plugin or extension architecture

## 14. Risks and Mitigations

### 14.1 Large Model and Dataset Sizes
Risk:
Local storage usage may become difficult for users to manage.

Mitigation:
Provide storage dashboards, path controls, disk usage visibility, and cleanup tools.

### 14.2 Hardware Variability
Risk:
Users may have systems that cannot run some training or conversion jobs effectively.

Mitigation:
Add hardware detection, preflight checks, and clear CPU/GPU fallback messaging.

### 14.3 Long-Running Job Failure
Risk:
Training and conversion jobs may fail after long runtimes.

Mitigation:
Use persistent logs, checkpointing, resumable workflows where supported, and reliable job state tracking.

### 14.4 Model Compatibility Fragmentation
Risk:
Different local model ecosystems may require different files and parameters.

Mitigation:
Use adapter-based model abstraction and explicit compatibility validation before job launch.

## 15. Release Recommendation

### 15.1 Suggested Delivery Phases
Phase 1:
- Core shell, local storage, project management, downloader, GPU detection, separation, conversion, and export

Phase 2:
- Training workflows, richer dataset tooling, resume-capable jobs, advanced settings, and power-user diagnostics

Phase 3:
- Workflow presets, batch automation, expanded model-family support, and advanced editing tools

## 16. Summary
VoiceAI Studio should be built as a secure, local-first Windows desktop application that combines Electron, React, and Python into a privacy-preserving audio AI workstation. The architecture should prioritize local execution, strong job orchestration, resilient storage management, and a clean UX for heavy computational workflows.
