import { API } from "../constants";

async function createShortUrl(url, lifetime) {
  const result = await fetch(`${API}/oneways/create`, {
    method: "post",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      target: url,
      is_temporary: true,
      lifetime: lifetime,
      only_numbers: false,
      user_uid: null
    }),
  });

  return await result.json();
}

async function updateShortUrl(uid, alias) {
  const result = await fetch(`${API}/oneways/update`, {
    method: "post",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      uid: uid,
      alias: alias,
    }),
  });

  return await result.json();
}

async function getRedirectUrl(alias) {
  const result = await fetch(`${API}/oneways/${alias}`, {
    method: "get",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
  });

  return await result.json();
}

export { createShortUrl, updateShortUrl, getRedirectUrl };
