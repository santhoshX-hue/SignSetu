// Base API service for offline local backend
export const API_BASE_URL = 'http://127.0.0.1:8000';

export async function checkBackendHealth() {
  const response = await fetch(`${API_BASE_URL}/api/health`);
  return await response.json();
}
