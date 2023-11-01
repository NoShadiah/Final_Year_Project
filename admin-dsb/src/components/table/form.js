import React from "react";
import { useState, useEffect } from "react";
// import "./table.css";

// export function table(){
//     const fields = [];
//     fields.push(this.props.first)
//     return(
//         <section className="section">
//         <div class="table-box">
//             <div class="table-value">
//                 <table onSubmit={()=>{navigate("/dashboard")}}>
//                     <h2>Add</h2>
//                     <p> Enter all required details to add<br></br>item</p>
//                     <div class="inputbox">
//                         {/* <!-- from fontawesome i will get the icons for the input labels --> */}
//                         <label for="email">Email: </label>
//                         {/* <i class="fas fa-envelope"></i> */}
//                         <input type="email" required name="email"/>
//                         {fields?.map(
//                             <label for={props.name}>{props.name}</label>
//                         )
//                     }
                        
//                     </div>
//                     <button id="button">Add</button>
//                     <div classname="register">
//                         <p><a href="/">Cancel</a></p>
//                     </div>

//                 </table>
//             </div>
//         </div>
//     </section>
//     )
// }


export function Table({dictionaries, endpoint, title}){
    const [tableData, settableData] = useState({});
    // const [title, setTilte] = useState("")
    // const [endpoint, se]

    const handleChange = (e, fieldname) => {
      settableData({ ...tableData, [fieldname]: e.target.value });
    };
  
    const handleSubmit = (e) => {
      e.preventDefault();
      // You can now access the table data in the `tableData` object
      console.log('table Data:', tableData);
  
      // If endpoint is provided, you can make a POST request to it.
      if (endpoint) {
        fetch(endpoint, {
          method: 'POST',
          body: JSON.stringify(tableData),
          headers: {
            'Content-Type': 'application/json',
          },
        })
          .then((response) => response.json())
          .then((data) => {
            console.log('Data posted successfully:', data);
          })
          .catch((error) => {
            console.error('Error posting data:', error);
          });
      }
      // setTilte("");
      settableData([]);
      
    };
  
    useEffect(() => {
      // Optionally, you can pertable other actions when the component mounts
      // or when the dictionaries or endpoint change.
    }, [dictionaries, endpoint, title]);
  
    return (

      <table onSubmit={handleSubmit}>
        <h1>Enter {title} details</h1>
        <div id="tabledivs">
        {
            dictionaries?.map(dict => (
          <div className="inputbox">
            <label for={dict.fieldname}>{dict.fieldname}:</label>
            <input
              type={dict.datatype}
              id={dict.fieldname}
              name={dict.fieldname}
              value={tableData[dict.fieldname] || ''}
              onChange={(e) => handleChange(e, dict.fieldname)} required
            />
          </div>
        )
      )
    }
        </div>
        
        <button id="button">Submit</button>
      </table>
    );
  }
  