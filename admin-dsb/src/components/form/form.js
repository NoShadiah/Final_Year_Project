import React from "react";
import { useState, useEffect } from "react";
// import "./form.css";

// export function Form(){
//     const fields = [];
//     fields.push(this.props.first)
//     return(
//         <section className="section">
//         <div class="form-box">
//             <div class="form-value">
//                 <form onSubmit={()=>{navigate("/dashboard")}}>
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

//                 </form>
//             </div>
//         </div>
//     </section>
//     )
// }


export function Form({dictionaries, endpoint, title}){
    const [formData, setFormData] = useState({});
    // const [title, setTilte] = useState("")
    // const [endpoint, se]

    const handleChange = (e, fieldname) => {
      setFormData({ ...formData, [fieldname]: e.target.value });
    };
  
    const handleSubmit = (e) => {
      e.preventDefault();
      // You can now access the form data in the `formData` object
      console.log('Form Data:', formData);
  
      // If endpoint is provided, you can make a POST request to it.
      if (endpoint) {
        fetch(endpoint, {
          method: 'POST',
          body: JSON.stringify(formData),
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
      setFormData([]);
      
    };
  
    useEffect(() => {
      // Optionally, you can perform other actions when the component mounts
      // or when the dictionaries or endpoint change.
    }, [dictionaries, endpoint, title]);
  
    return (

      <form onSubmit={handleSubmit}>
        <h1>Enter {title} details</h1>
        <div id="formdivs">
        {
            dictionaries?.map(dict => (
          <div className="inputbox">
            <label for={dict.fieldname}>{dict.fieldname}</label>
            <input
              type={dict.datatype}
              id={dict.fieldname}
              name={dict.fieldname}
              value={formData[dict.fieldname] || ''}
              onChange={(e) => handleChange(e, dict.fieldname)}
            />
          </div>
        )
      )
    }
        </div>
        
        <button id="button">Submit</button>
      </form>
    );
  }
  