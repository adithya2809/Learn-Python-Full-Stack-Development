

function Welcome(props){
  return <h1>Welcome {props.name}</h1>
  
}


function App(){
  return(
    <>
    <Welcome name="Adithya"/>
    <Welcome name="Paul"/>
    <Welcome name="Caraxes"/>
    </>
  );

}
export default App;