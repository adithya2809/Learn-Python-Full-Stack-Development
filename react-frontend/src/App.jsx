import {useState} from "react";


function App(){
  const [formData,setFormData]=useState({
    "username":"",
    "email":"",
    "password":""
  });

  function handleChange(event){
    const{name,value}=event.target;

    setFormData({
      ...formData,
      [name]:value
    });

  }
  async function handleSubmit(event){
    event.preventDefault();
    const response=await fetch("http://localhost:8000/auth/register",{
      method:"POST",
      headers:{
        "Content-Type":"application/json"
      },
      body:JSON.stringify(formData)
    }
    );

    const data=await response.json();
    console.log("Status:",response.status);
    console.log("Response:",data);
  }

  return(
    <>
    <form onSubmit={handleSubmit}>
      <input type="text" name="username" value={formData.username} 
      onChange={handleChange}/>

      <input type="email" name="email" value={formData.email} 
      onChange={handleChange} />

      <input type="password" name="password" value={formData.password}
      onChange={handleChange} />

      <button type="submit">Register</button>

    </form>

    </>

    
  );

}
export default App;