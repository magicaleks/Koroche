import "./ServicePage.css";

const time_list = {
    1: "3",
    2: "24",
    3: "72",
    4: "168"
};

function ServicePage (timeValue, setTimeValue, linkName, setLinkName, newLinkName, setNewLinkName) {

    async function createLink (event) {
        let response = await fetch("http://83.147.246.113/api/v1/oneways/create", {
            method: "POST",
            headers: {
                "accept": "application/json",
                "Content-Type": "application/json"
            },
            body: `{
                "target": "${linkName}",
                "is_temporary": true,
                "lifetime": ${time_list[timeValue]},
                "user_uid": null,
                "only_numbers": true
            }`
        });

        let data = await response.json();

        console.log(data);
        
        setLinkName("https://koroche.app/");
    }

    return <div class="ServicePage">

        <div>
            <p>select the time the link is active:</p>
            <select id="time" defaultValue={timeValue} onChange={event => setTimeValue(event.target.value)}>
                <option value="1">3 hours</option>
                <option value="2">24 hours</option>
                <option value="3">3 days</option>
                <option value="4">7 days</option>
            </select>
        </div>
        <div>
            <p>type your link:</p>
            <input type="text" value={linkName} onChange={event => setLinkName(event.target.value)}/>
        </div>
        <button onClick={createLink}>сделать ссылку koroche</button>

    </div>;

}

export default ServicePage;