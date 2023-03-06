import React, {useEffect, useState} from "react";

//useState is going to be used for setting data from the API and providing into the jsx for showing the data.
// useEffect is going to be used for rendering a fetch method on a single reload.
function App() {
  //The useState hook is to track the current state of the data
  const[data, setData] = useState({
        id:"", 
        title:"",
        purchase_date:"", 
        author:""
  });
  // The useEffect hook is to be used for single rendering
  useEffect(()=>{
    // Using fetch to fetch the api from flask server it will be redirected to proxy
    fetch("/book_data").then((res)=>
        res.json().then((data)=>{
          // setting a data from the api
          setData({
          id:data.Id, 
          title:data.Title,
          purchase_date:data.Purchase_date, 
          author:data.Author
        });
      })
    );

  }, []);
  return (
    <div className="App">
      <header className="App-header">
        <h1>React and Flask</h1>
        {/* Calling data from setData for showing the dtaa from the endpoint*/}
        <p>{data.id}</p>
        <p>{data.title}</p>
        <p>{data.purchase_date}</p>
        <p>{data.author}</p>
      </header>
    </div>
  );
}

export default App;
