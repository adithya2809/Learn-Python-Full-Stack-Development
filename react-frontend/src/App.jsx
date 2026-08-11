import {useState,useEffect} from "react";


function App(){
  
  const [students,setStudents]=useState([]);
  useEffect(()=>{
    async function getStudents(){
      const response=await fetch("http://localhost:8000/students");
      const data=await response.json();

      setStudents(data);

    }
    getStudents();
  },[]);
  const [formData,setFormData]=useState({
    "username":"",
    "email":"",
    "password":""
  });

  const [message,setMessage]=useState("");
  const [error,setError]=useState("");
  const [loading,setLoading]=useState(false);

  
  function handleChange(event){
    const{name,value}=event.target;

    setFormData({
      ...formData,
      [name]:value
    });

  }
  async function handleSubmit(event){
    event.preventDefault();

    setMessage("");
    setError("");
    setLoading(true);
    try{
    const response=await fetch("http://localhost:8000/auth/register",{
      method:"POST",
      headers:{
        "Content-Type":"application/json"
      },
      body:JSON.stringify(formData)
    }
    );
  

    const data=await response.json();
    if (response.ok){
      setMessage("Registration Successful!");
    }
    else {
      setError(data.detail)
    }
  }
    catch (error){
      setError("Unable to connect to the server");
    }finally {
      setLoading(false);
    }
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

      <button type="submit" disabled={loading}>{loading?"Registering":"Register"}</button>

      {message&&<p>{message}</p>}
      {error&&<p>{error}</p>}
    </form>
    <h1>Students</h1>
    {students.map((student)=>(
      <p key={student.id}>{student.name}</p>
    ))}
    </>

  );
  

}
export default App;