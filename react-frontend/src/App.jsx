import {useState} from "react";




function App(){
  const[username,setUserame]=useState("");
  const[email,setEmail]=useState("");
  const[password,setPassword]=useState("");

  function handleSubmit(event){
    event.preventDefault();

    console.log(username);
    console.log(email);
    console.log(password);
  }

  return(
    <>
    <form onSubmit={handleSubmit}>
      <input type="text" value={username} 
      onChange={(event)=> setUsername(event.target.value)}/>

      <input type="email" value={email} 
      onChange={(event)=> setEmail(event.target.value)} />

      <input type="password" value={password}
      onChange={(event) => setPassword(event.target.value)} />
    </form>

    <button type="submit">Register</button>
    </>

    
  );

}
export default App;