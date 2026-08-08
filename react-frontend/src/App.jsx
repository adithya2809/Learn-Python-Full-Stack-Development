import { useState} from "react";




function App(){
  const[count,setCount]=useState(0);

  return(
    <>
    <h1>Count:{count}</h1>

    <button onClick={() => {
    setCount(count+1);
    }}>
      Increase
    </button>
    <button onClick={() => {
      setCount(count>0?count-1:0);
    }}>
      Decrease
    </button>

    <button onClick={()=>{
      setCount(0)
    }}>
      Reset
    </button>
    <button onClick={()=>{
      setCount(count>0?count*2:count+1);
    }}>
      Increase by 2
    </button>
    <p>{count===0? "count is at zero":"You're counting"}</p>
    <p>{count>=10?"You've reached 10":"Keep going!"}</p>
    </>
  );

}
export default App;