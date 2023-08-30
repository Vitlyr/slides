import React, { useState } from "react";
import ReactDOM from "react-dom";
import settings from "/settings.py";

const App = () => {
    const [slides] = useState(settings.slides);
    const [timing] = useState(settings.timing);
    const [scount] = useState(settings.scount);
    return (
        <div>
            <h3>{slides[1]}</h3>
            <h3>{timing}</h3>
            <h3>{scount}</h3>
        </div>
    );
};

ReactDOM.render(<App />, document.getElementById("root"));
