import React, { Component } from 'react';

class App extends Component {
    state = {
        todos: []
    };

    async componentDidMount() {
        try {
            const res = await fetch('http://web:8976/api/');
            const res = await res.json();
            this.setState({
                todos
            });
        } catch (e) {
            console.log(e)
        }
    }

    render() {
        return (
            <div>
                {this.state.todos.map( item => (
                    <div key = {item.id}>
                        <h1>{item.title}</h1>
                        <span>{item.description}</span>
                    </div>
                ))}
            </div>
        );
    }
}

export default App
