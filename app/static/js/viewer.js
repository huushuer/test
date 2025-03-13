const socket = io();
let peerConnection;
const servers = { iceServers: [{ urls: "stun:stun.l.google.com:19302" }] };
const remoteVideo = document.getElementById("remoteVideo");

socket.on("offer", async (offer) => {
    peerConnection = new RTCPeerConnection(servers);
    peerConnection.ontrack = event => remoteVideo.srcObject = event.streams[0];

    peerConnection.onicecandidate = event => {
        if (event.candidate) socket.emit("candidate", event.candidate);
    };

    await peerConnection.setRemoteDescription(new RTCSessionDescription(offer));
    const answer = await peerConnection.createAnswer();
    await peerConnection.setLocalDescription(answer);
    socket.emit("answer", answer);
});

socket.on("candidate", async (candidate) => {
    if (!peerConnection) return;
    await peerConnection.addIceCandidate(new RTCIceCandidate(candidate));
});