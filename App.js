import React from "react";
import { MDBContainer, MDBRow, MDBCol } from "mdbreact";
import './App.css'; //Import here your file style
import { Container, Row, Col } from "react-grid-system";
import axios from "axios";


class App extends React.Component{
  constructor(props) {
    super(props);
    this.state = {data:'', data2:''};
  }
  componentDidMount() {
    fetch("http://127.0.0.1:5000/layers",{headers : { 
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      "mode":'no-cors',
      "Access-Control-Allow-Origin":"http://127.0.0.1/5000/layers"
     }})
    .then(r => r.json())
    .then(r => {
        console.log(r)
        this.setState({
          data:r
          })
          
    })
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json',"Access-Control-Allow-Origin":"http://127.0.0.1/5000/layers",'Accept': 'application/json',
      "mode":'no-cors'}
      
      
  };
  fetch('http://127.0.0.1/5000/layers', requestOptions)
      .then(r => r.json())
      .then(data => this.setState({ data2: data }));
}
      
    
    
   
  
  render(){
    const data = Array.from(this.state.data);
    const arr = Array()
    for (var i=0;i<data.length;i++){
      const a = Array()
      for(var x=0;x<data[i];x++){
        a.push(<button style={{borderRadius:'100%'}}></button>)
      }
      arr.push(a)
      
    }
    return(
      <div className={"Test"}> 
      <div style={{verticalAlign:'middle', background:'#666'}}>
        <ul style={{listStyleType:'none', background:'#666'}}>{arr.map((item)=>{
          return (<div style={{borderStyle:'solid', width:'1%', float:'left', background:'#666', padding:'5px',margin:'10px'}}>L {arr[arr.indexOf(item)].length}<br></br>{item}</div>
              
          )
        })}</ul>
        <div>Test</div>
        
      </div>
      </div>
      
    )
  }
}

export default App;