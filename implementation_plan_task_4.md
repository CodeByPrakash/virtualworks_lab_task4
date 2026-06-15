# Quote Generator with History - Implementation Plan

This plan outlines the approach for building the Quote Generator application (Task 4) which involves external API integration, local database storage, and utilizing the Stitch MCP to design the frontend UI.

## Architecture & Technology Stack
- **Frontend Design (Stitch MCP):** I have successfully created a new Stitch project named `task_4` (Project ID: 3997917304987450). I will use Stitch's generative capabilities to create a beautiful, interactive screen for the Quote Generator.
- **Backend (Flask):** A local Python server to manage data.
- **Database (SQLite):** To store the history of generated quotes.
- **External API:** We will use a public API (e.g., `api.quotable.io` or `zenquotes.io/api/random`) to fetch random quotes.

## Proposed Changes

### Phase 1: Frontend UI Generation (Stitch)
- Use the Stitch MCP (`mcp_stitch_generate_screen_from_text`) to generate a UI screen that features:
  - A prominent display area for the random quote and its author.
  - A "Generate New Quote" button.
  - A "History" section or sidebar that lists previously fetched quotes.
- I will share the link/details of the generated UI with you.

### Phase 2: Local Backend Implementation (Optional / If Needed Locally)
#### [NEW] `task_4/app.py`
A Flask application providing:
- `GET /api/quote` - Fetches a random quote from the external API, saves it to the local SQLite database, and returns the quote to the frontend.
- `GET /api/history` - Returns a list of all previously saved quotes from the database.

#### [NEW] `task_4/requirements.txt`
Dependencies:
- `Flask`
- `requests` (for calling the external API from the backend)

### Phase 3: Integration
- Depending on the output from Stitch, we can either extract the generated React/HTML code into the `task_4/templates` directory and hook it up to our Flask backend, or simply review the design in Stitch.

## Verification Plan
- Generate the screen in Stitch and verify the visual layout.
- Start the Flask backend and test the API endpoints (`/api/quote` and `/api/history`) to ensure data is correctly fetched from the external API and saved locally.

## User Review Required
> [!IMPORTANT]
> Since we are using the Stitch MCP for the UI, would you like me to extract the generated frontend code and wire it up to a local Flask backend so you can run the full app locally (like Tasks 1-3)? Or do you just want to generate and view the UI design within Stitch? I will proceed with generating the UI in Stitch as soon as you approve!
