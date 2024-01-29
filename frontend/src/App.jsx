import { useCallback, useState } from "react";
import { nanoid } from "nanoid";
import { createShortUrl, updateShortUrl } from "./api/request";
import { DROPDOWN_OPTIONS, SHORT_URL_START } from "./constants";
import { isValidUrl } from "./utils/validator";

import "./App.css";

function App() {
  const [link, setLink] = useState(""); // первая ссыока
  const [shortLink, setShortLink] = useState(null); // короткая ссылка
  const [error, setError] = useState(true); // если неправильная ссылка
  const [currentDropdownOption, setCurrentDropdownOption] = useState({ value: 0, label: "поменять время" }); // Для работы со временем

  const [uuid, setUUid] = useState(null);

  // добавляем uid в хранилище
  if (!localStorage.getItem("user_uid")) {
    localStorage.setItem("user_uid", nanoid());
  }

  const onChangeDropdown = useCallback((option) => {
    setCurrentDropdownOption(option);
  }, []);

  const inputHandler = (value) => {
    setLink(value);
    setError(!isValidUrl(value));
  };

  async function createShortLinkHandler(e) {
    e.preventDefault();
    const { uid, alias } = await createShortUrl(link, currentDropdownOption?.value);
    setUUid(uid);
    setShortLink(alias);
  }

  async function updateShortLinkHandler(e) {
    e.preventDefault();
    const newLink = await updateShortUrl(uuid, shortLink);
    setShortLink(newLink);
  }

  console.log(currentDropdownOption);
  return (
    <>
      <header className="header">
        <h1>
          <a href="/">Koroche</a>
        </h1>
      </header>
      <main>
        <form>
          {shortLink !== null ? (
            <>
              <label>Edit URL:</label>
              <div className="container-shortURL">
                {SHORT_URL_START}
                <input type="text" required value={shortLink} onChange={(e) => setShortLink(e.target.value)} />
              </div>
              <button type="submit" onClick={(e) => updateShortLinkHandler(e)} disabled={!shortLink}>
                Обновить алиас
              </button>
            </>
          ) : (
            <>
              <label htmlFor="url">Введите длинный URL:</label>
              <div className="container">
                <input
                  type="url"
                  name="url"
                  required
                  autoComplete="off"
                  value={link}
                  placeholder="Пример: https://длинная-ссылка.рф/"
                  onChange={(e) => inputHandler(e.target.value)}
                />
                <div className="btn-group">
                  {DROPDOWN_OPTIONS.map((option) => {
                    return (
                      <button
                        key={option.label}
                        type="button"
                        className={option.value === currentDropdownOption.value ? "active" : ""}
                        onClick={() => onChangeDropdown(option)}
                      >
                        {option.label}
                      </button>
                    );
                  })}
                </div>
              </div>
              <button type="submit" className={error ? "invalid" : "valid"} onClick={(e) => createShortLinkHandler(e)} disabled={error}>
                Сделать короче
              </button>
            </>
          )}
        </form>
      </main>
    </>
  );
}

export default App;
