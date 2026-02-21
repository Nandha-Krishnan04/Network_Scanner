from flask import Flask, render_template, jsonify
import scanner
import hostdetails

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/scan")
def scan():
    my_ip = hostdetails.get_myip()
    network = '.'.join(my_ip.split('.')[:-1]) + '.0/24'
    hosts = scanner.arp_scan(network)

    return jsonify({
        "my_ip": my_ip,
        "hosts": hosts
    })

if __name__ == "__main__":
    app.run(debug=True)