from rest_framework.test import APITestCase
from django.urls import reverse


class NotesCrudTests(APITestCase):
    def test_health_ok(self):
        url = reverse('Health')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), {"status": "ok"})

    def test_create_list_retrieve_update_delete(self):
        # Create
        res = self.client.post("/api/notes/", {"title": "First", "content": "Hello"}, format="json")
        self.assertEqual(res.status_code, 201, res.content)
        note_id = res.json()["id"]

        # List
        res = self.client.get("/api/notes/")
        self.assertEqual(res.status_code, 200)
        self.assertTrue("results" in res.json())
        self.assertGreaterEqual(len(res.json()["results"]), 1)

        # Retrieve
        res = self.client.get(f"/api/notes/{note_id}/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()["title"], "First")

        # Update
        res = self.client.patch(f"/api/notes/{note_id}/", {"title": "Updated"}, format="json")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()["title"], "Updated")

        # Delete
        res = self.client.delete(f"/api/notes/{note_id}/")
        self.assertEqual(res.status_code, 204)
