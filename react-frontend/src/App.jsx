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
  function handleSubmit(event){
    event.preventDefault();

    console.log(formData);
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