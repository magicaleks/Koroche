import "./Header.css";

function Header (current_page, setPage) {
  
    function changePage(page) {
        setPage(page);
    }

    return <header>

        <h1 class="logo">Koroche</h1>

        <nav>
            <ul>
                <li id="landing" className={current_page === "landing" ? "active" : ""} onClick={() => changePage("landing")}>Info</li>
                <li id="servicePage" className={current_page === "servicePage" ? "active" : ""} onClick={() => changePage("servicePage")}>Create link</li>
            </ul>
        </nav>

        <div class="empty"></div>

    </header>;
}

export default Header;