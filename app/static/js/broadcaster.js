const socket = io();
let localStream;
let peerConnection;
const servers = { iceServers: [{ urls: "stun:stun.l.google.com:19302" }] };

async function startBroadcast() {
    try {
        localStream = await navigator.mediaDevices.getUserMedia({
            video: { facingMode: "environment" }, //バックカメラ設定
            audio: true
        });
        document.getElementById("localVideo").srcObject = localStream;

        peerConnection = new RTCPeerConnection(servers);
        localStream.getTracks().forEach(track => peerConnection.addTrack(track, localStream));

        peerConnection.onicecandidate = event => {
            if (event.candidate) socket.emit("candidate", event.candidate);
        };

        const offer = await peerConnection.createOffer();
        await peerConnection.setLocalDescription(offer);
        socket.emit("offer", offer);
    } catch (error) {
        console.error("カメラロードエラー:", error);
    }
}

socket.on("answer", async (answer) => {
    if (!peerConnection) return;
    await peerConnection.setRemoteDescription(new RTCSessionDescription(answer));
});

socket.on("candidate", async (candidate) => {
    if (!peerConnection) return;
    await peerConnection.addIceCandidate(new RTCIceCandidate(candidate));
});

startBroadcast();