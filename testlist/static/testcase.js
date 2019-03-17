$(function() {
    // When we're using HTTPS, use WSS too.
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var chatsock = new WebSocket(ws_scheme + '://' + window.location.host + "/ws/testlist/testcase/");
});