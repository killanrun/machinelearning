import React from 'react';
import './App2.css';


class App2 extends React.Component{
    constructor(props){
        super(props);
        this.state={data:''};
    }
    render(){
        return(
            <div>
            <div className="Sidebar"></div>
            <div className="Tile" >Network Error</div>
            <div className="Tile" >Testing</div>
            <div className="Tile" >Testing</div>
            </div>




        )
    }




}
export default App2;