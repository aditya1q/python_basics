import { useEffect, useState } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const [todos, setTodos] = useState([]);
  const [tasks, setTasks] = useState('');

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/api/todos')
      .then(res => {
        setTodos(res.data)
      })
      .catch(error => console.error('Error fetching todos:', error));
  }, []);

  const addTask = async (e) => {
    e.preventDefault();
    if (!tasks.trim()) return;

    try {
      const res = await axios.post('http://127.0.0.1:5000/api/todos', { task: tasks });
      console.log(res)
      setTodos([...todos, res.data]);
      setTasks('');
    } catch (error) {
      console.error('Error adding task:', error);
    }
  };

  const toggleTask = async (id) => {
    const updatedTodos = todos.map(task =>
      task.id === id ? { ...task, done: !task.done } : task
    );
    setTodos(updatedTodos);

    try {
      await axios.put(`http://127.0.0.1:5000/api/todos/${id}`, {
        done: !todos.find(task => task.id === id).done
      });
    } catch (error) {
      console.error('Error updating task:', error);
    }
  };

  const removeTask = async (id) => {
    try {
      await axios.delete(`http://127.0.0.1:5000/api/todos/${id}`);
      setTodos(todos.filter(task => task.id !== id));
    } catch (error) {
      console.error('Error deleting task:', error);
    }
  };

  return (
    <main className="bg-black min-h-screen text-white flex justify-center items-center p-4">
      <div className="w-full max-w-xl p-6 bg-gray-900 rounded-2xl shadow-lg">
        <h1 className="text-3xl font-bold mb-6 text-center tracking-tight">To-Do List</h1>

        <form onSubmit={addTask} className="flex mb-6 gap-3">
          <input
            type="text"
            value={tasks}
            onChange={(e) => setTasks(e.target.value)}
            placeholder="Add a new task..."
            className="flex-1 p-3 rounded-lg bg-gray-800 text-white border border-gray-700 focus:outline-none focus:border-blue-600 transition-colors placeholder-gray-500"
          />
          <button
            type="submit"
            className="px-6 py-3 bg-blue-600 rounded-lg hover:bg-blue-700 transition-all duration-200 font-medium cursor-pointer"
          >
            Add
          </button>
        </form>

        <ul className="space-y-3">
          {todos.map((task) => (
            <li
              key={task.id}
              className="flex justify-between items-center bg-gray-800 p-4 rounded-lg hover:bg-gray-750 transition-colors duration-150"
            >
              <div className="flex items-center gap-3">
                <input
                  type="checkbox"
                  checked={task.done}
                  onChange={() => toggleTask(task.id)}
                  className="w-5 h-5 text-blue-600 bg-gray-700 border-gray-600 rounded focus:ring-blue-600"
                />
                <span className={`${task.done ? 'line-through text-gray-500' : 'text-white'}`}>
                  {task.task}
                </span>
              </div>
              <button
                onClick={() => removeTask(task.id)}
                className="text-red-500 hover:text-red-700 text-xl font-bold transition-colors duration-150 cursor-pointer"
              >
                ✕
              </button>
            </li>
          ))}
        </ul>
      </div>
    </main>
  );
}

export default App;
