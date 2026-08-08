import { useState} from "react";




function App(){
  const[count,setCount]=useState(0);

  function increase(){
    setCount(count+1)
  }

  function decrease(){
    setCount(count>0?count-1:0)
  }

  function reset(){
    setCount(0)
  }
  return(
    <>
    <h1>Count:{count}</h1>

    <button onClick=
    {increase}
    >
      Increase
    </button>
    <button onClick=
      {decrease}
    >
      Decrease
    </button>

    <button onClick={reset}>
      Reset
    </button>
    <button onClick={()=>{
      setCount(count>0?count*2:count+1);
    }}>
      * 2
    </button>
    <p>{count===0? "count is at zero":"You're counting"}</p>
    <p>{count>=10?"You've reached 10":"Keep going!"}</p>

    
    </>

    
  );

}
export default App;