# note-management-system-45451-45460

Backend: Django + DRF notes CRUD API

Quick start:
- Python 3.11+
- Dependencies are pinned in note_app_backend/requirements.txt
- Default DB is SQLite. To use another DB, set DATABASE_URL env var.

Setup
1) cd note-management-system-45451-45460/note_app_backend
2) pip install -r requirements.txt
3) python manage.py migrate
4) python manage.py runserver 0.0.0.0:3001

Health
- GET /api/health/ -> {"status":"ok"}

Notes API
- POST /api/notes/
  body: {"title":"My note","content":"optional"}
- GET /api/notes/?q=term&page=1&page_size=10
- GET /api/notes/{id}/
- PUT /api/notes/{id}/
- PATCH /api/notes/{id}/
- DELETE /api/notes/{id}/

Ordering
- Default ordering is -updated_at

Docs/OpenAPI
- Swagger UI: /api/docs/
- OpenAPI JSON: /api/schema/

Examples
- Create:
  curl -s -X POST http://localhost:3001/api/notes/ -H "Content-Type: application/json" -d '{"title":"First","content":"Hello"}'
- List:
  curl -s http://localhost:3001/api/notes/
- Search:
  curl -s "http://localhost:3001/api/notes/?q=First"
- Retrieve:
  curl -s http://localhost:3001/api/notes/1/
- Update:
  curl -s -X PATCH http://localhost:3001/api/notes/1/ -H "Content-Type: application/json" -d '{"title":"Updated"}'
- Delete:
  curl -s -X DELETE http://localhost:3001/api/notes/1/

Environment variables
- DATABASE_URL (optional): e.g. postgres://user:pass@host:5432/dbname
- PAGE_SIZE (optional): default 10

Style/theme
- Ocean Professional (comments only; API is headless)