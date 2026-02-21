function startScan() {

    let status = document.getElementById("status");
    let table = document.querySelector("#results tbody");

    status.innerText = "Searching network...";
    table.innerHTML = "";

    fetch("/scan")
    .then(response => response.json())
    .then(data => {

        status.innerText = "Scan Complete ✔";

        let myIP = data.my_ip;
        let hosts = data.hosts;

        hosts.forEach(host => {

            let highlightClass = host.ip === myIP ? "highlight" : "";

            let row = `
                <tr class="${highlightClass}">
                    <td>${host.ip}</td>
                    <td>${host.mac}</td>
                    <td>${host.vendor}</td>
                    <td>${host.device}</td>
                    <td>${host.hostname}</td>
                </tr>
            `;

            table.innerHTML += row;
        });

    })
    .catch(error => {
        status.innerText = "Error during scan!";
    });
}