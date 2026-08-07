import { useState} from "react";




function App(){
  const[count,setCount]=useState(0);

  return(
    <>
    <h1>Count:{count}</h1>

    <button onClick={() => {console.log("before:",count);
    setCount(count+1);
    console.log("after:",count);
    }}>
      Increase
    </button>
    </>
  );

}
export default App;