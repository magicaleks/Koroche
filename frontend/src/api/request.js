import { API } from "../constants";

async function createShortUrl(url, lifetime) {
  const result = await fetch(`${API}/create`, {
    method: "post",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      target: url,
      is_temporary: true,
      lifetime,
      user_uid: localStorage.getItem("user_uid"),
      only_numbers: true,
    }),
  });

  return await result.json();
}

async function updateShortUrl(uid, alias) {
  const result = await fetch(`${API}/update`, {
    method: "post",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      uid,
      alias,
    }),
  });

  return await result.json();
}

export { createShortUrl, updateShortUrl };
