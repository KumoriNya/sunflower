import React from "react";
import Websocket from "websocket";

function HomePage () {
    const [socket, setSocket] = React.useState<WebSocket|null>();
    const [content, setContent] = React.useState<string>("");

    React.useEffect(() => {
        // TOOD: find an unused socket to replace 8000
        console.log("Attempting to connect with socket")
        const ws = new WebSocket('ws://124.150.73.239:8000')
        ws.onopen = () => {
            console.log('Connection opened')
        }

        ws.onmessage = (event) => {
            const message = event.data
            console.log(`Message received: ${message}`)
            setContent((prevContent) => {
                const updatedContent = prevContent + message;
                const words = updatedContent.split(" ");
        
                if (words.length > 120) {
                  words.shift();
                  const croppedContent = words.join(" ");
                  return croppedContent;
                }
        
                return updatedContent;
            });
            // handle what to do with the msg
        }

        ws.onclose = () => {
            console.log('Connection closed')
        }

        setSocket(ws);
        const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));

        async function handleBeforeUnload (event: Event) {
            event.preventDefault();
            console.log('About to close the socket')
            ws.close();
            console.log('Should have closed the socket')
            const returnValue = "Anything you wanna put here!";
            return returnValue;
        // Custom logic to handle the refresh
        // Display a confirmation message or perform necessary actions
        };
        window.addEventListener('beforeunload', handleBeforeUnload);
        return () => {
            console.log("event listner removiong")
            window.removeEventListener('beforeunload', handleBeforeUnload);
            console.log("event listner removed")
            if (ws.readyState === 1) { // <-- This is important
                console.log("Connection closed by return")
                ws.close();
            }
        };

        // return () => {
        //     if (ws.readyState === 1) { // <-- This is important
        //         ws.close();
        //     }
        // };
    }, [])
    return (
    <>
        {/* Container for message */}
        Live Caption:
        <div>
            <p>{content}</p>
        </div>
    </>)
}

export default HomePage