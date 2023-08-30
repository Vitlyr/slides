import React from "react";
import settings from "/static/settings.py";

const App = () => {
  const [slides] = useState(settings.slides);
  const [timing] = useState(settings.timing);
  const [scount] = useState(settings.scount);
  return (
<html>
    <head>
        <title>Announcement(s)</title>
    </head>
    <body>
        <h3>{slides[1]}</h3>
        <h3>{timing}</h3>
        <h3>{scount}</h3>
    </body>
</html>
  );
};

export default App;
