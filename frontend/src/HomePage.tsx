import React from "react";
import Websocket from "websocket";

function HomePage () {
    const [socket, setSocket] = React.useState<null|WebSocket>();
    const [content, setContent] = React.useState<string>("");

    React.useEffect(() => {
        // TOOD: find an unused socket to replace 8000
        const ws = new WebSocket('ws://192.168.1.2:8000')
        ws.onopen = () => {
            console.log('Connection opened')
        }

        ws.onmessage = (event) => {
            const message = event.data
            // console.log(`Message received: ${message}, type = ${typeof(message)}, content is ${content}`)
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

        return () => {
            ws.close();
        };
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