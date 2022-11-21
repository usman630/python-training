<!DOCTYPE html>
<html>

<head>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous" />
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
</head>

<body>
    <div class="dark-background text-center">
        <div>
            <img id="bulbimg" src="https://d1tgh8fmlzexmh.cloudfront.net/ccbp-dynamic-webapps/bulb-go-on-img.png" class="bulb-image" />
        </div>
        <div>
            <img id="catimg" src="https://d1tgh8fmlzexmh.cloudfront.net/ccbp-dynamic-webapps/cat-img.png" class="cat-image" />
        </div>
        <div class="d-flex flex-row justify-content-center pt-5">
            <div class="switch-board">
                <h1 class="switch-status" id="usman">Switched On</h1>
                <button id="offSwitch" class="off-switch" onclick="switchOff()">OFF</button>
                <button id="onSwitch" class="on-switch" onclick="switchOn()">ON</button>
            </div>
        </div>
    </div>
</body>
</html>

................
css.....

.dark-background {
    background-color: #0b0b0b;
}

.bulb-image {
    width: 150px;
}

.cat-image {
    width: 300px;
}

.switch-board {
    width: 294px;
    height: 139px;
    background-color: #7b8794;
    border-radius: 12px;
    padding-top: 32px;
    padding-bottom: 32px;
    padding-left: 16px;
    padding-right: 16px;
    margin: 16px;
}

.switch-status {
    font-family: "Roboto";
    font-weight: 500;
    font-size: 24px;
    color: #ffffff;
    margin-bottom: 24px;
}

.on-switch {
    font-family: "Roboto";
    font-weight: bold;
    font-size: 24px;
    color: #ffffff;
    border-radius: 8px;
    width: 99px;
    height: 44px;
    margin-left: 16px;
    background-color: #cbd2d9;
}

.off-switch {
    font-family: "Roboto";
    font-weight: bold;
    font-size: 24px;
    color: #ffffff;
    border-radius: 8px;
    width: 99px;
    height: 44px;
    background-color: #e12d39;
}

js..........................................................
function switchOff() {
    document.getElementById("bulbimg").src = "https://d1tgh8fmlzexmh.cloudfront.net/ccbp-dynamic-webapps/bulb-go-off-img.png";
    document.getElementById("catimg").src = "https://d1tgh8fmlzexmh.cloudfront.net/ccbp-dynamic-webapps/cat-eyes-img.png";
    document.getElementById("usman").textContent = "switched Off"
    document.getElementById("onSwitch").style.backgroundColor = "#22c55e";
    document.getElementById("offSwitch").style.backgroundColor = "#cbd2d9";
}


function switchOn() {

    document.getElementById("bulbimg").src = "https://d1tgh8fmlzexmh.cloudfront.net/ccbp-dynamic-webapps/bulb-go-on-img.png";
    document.getElementById("catimg").src = "https://d1tgh8fmlzexmh.cloudfront.net/ccbp-dynamic-webapps/cat-img.png";
    document.getElementById("usman").textContent = "switched On"
    document.getElementById("offSwitch").style.backgroundColor = "#e12d39";
    document.getElementById("onSwitch").style.backgroundColor = "#cbd2d9";
}
