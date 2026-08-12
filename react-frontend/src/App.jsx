import {useState,useEffect,useRef, useMemo} from "react";


function App(){
const [students, setStudents] = useState([]);
const [StudentLoading, setStudentLoading] = useState(true);
const [studentsError, setStudentsError] = useState("");

const [formData, setFormData] = useState({
  username: "",
  email: "",
  password: ""
});

const [message, setMessage] = useState("");
const [registerError, setRegisterError] = useState("");
const [registerLoading, setRegisterLoading] = useState(false);

const [count, setCount] = useState(0);

const inputRef=useRef(null);
const previousCount=useRef(null);
const [search,setSearch]=useState("")
const dragons=[
  {id:1,name:"Adhi"},
  {id:2,name:"caraxes"},
  {id:3,name:"sunfyre"}
  
];
  useEffect(()=>{ //NO dependacy
    async function getStudents(){
      try{
      const response=await fetch("http://localhost:8000/students");

      if(!response.ok){
        throw new Error("Failed to fetch students");
      }
      const data=await response.json();
    

      setStudents(data);

    }
    catch (error){
      setStudentsError("Unable to load students")
    }
    finally{
      setStudentLoading(false);
    }
  }
    getStudents();
},[]);


  useEffect(()=>{
    const timer=setInterval(() => {
      console.log("running")
    }, 100);
    return ()=> {
      clearInterval(timer);
    };
  },[]);
 

  useEffect(()=> {
    console.log("Effect ran. Count:",count);
  },[count]);

  useEffect(()=>{
    previousCount.current=count;
  },[count]);

  
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
    setRegisterError("");
    setRegisterLoading(true);
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
      setRegisterError(data.detail)
    }
  }
    catch (error){
      setRegisterError("Unable to connect to the server");
    }finally {
      setRegisterLoading(false);
    }
  }

  function focusInput(){
    inputRef.current.focus();
  }

  const filteredDragons=useMemo(()=>{
    console.log("filtering dragons...");
    return dragons.filter((dragons)=>
    dragons.name
          .toLowerCase()
          .includes(search.toLowerCase())
        );
      
  },[search])
  return(
    <>
     <form onSubmit={handleSubmit}>
      <input type="text" name="username" value={formData.username} 
      onChange={handleChange}/>

      <input type="email" name="email" value={formData.email} 
      onChange={handleChange} />

      <input type="password" name="password" value={formData.password}
      onChange={handleChange} />

      <button type="submit" disabled={registerLoading}>{registerLoading?"Registering":"Register"}</button>

      {message&&<p>{message}</p>}
      {registerError&&<p>{registerError}</p>}
    </form>
    
    <h1>{count}</h1>
    <button onClick={()=> setCount(count+1)}>
      Increase
    </button>

    <button onClick={()=> setCount(0)}>Reset</button>

    <h1>Students</h1>
    {StudentLoading && <p>Loading students...</p>}
    {studentsError && <p>{studentsError}</p>}
    {!StudentLoading &&
  !studentsError &&
  students.map((student) => (
    <p key={student.id}>
      {student.name}
    </p>
  ))}
  <input ref={inputRef} />
  <button onClick={focusInput}>Focus Input</button>

  <h1>Current:{count}</h1>
  <h2>Previous:{previousCount.current}</h2>
  
  <input value={search} 
  onChange={(event)=> setSearch(event.target.value)} 
  placeholder="Search dragons"/>

  {filteredDragons.map((dragons)=>(
    <p key={dragons.id}>{dragons.name}</p>
  ))}
    </>
  );
}
export default App;