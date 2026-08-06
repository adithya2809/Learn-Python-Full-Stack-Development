

function Student({name, age,course}){
  return(<> <h1>{name}</h1>
        <h2>{age}</h2>
        <p>{course}</p>
  </>

  )
  
}


function App(){
  return(
    <>
    <Student name="Adithya"
             age={25}
             course="React"/>
    <Student name="Paul"
             age={35}
             course="Duke"/>
    <Student name="Caraxes"
             age={75}
             course="Obey"/>
    
    </>
  );

}
export default App;