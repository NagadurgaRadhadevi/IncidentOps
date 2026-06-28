import { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";

const API = "http://127.0.0.1:8000";

function App() {

  const [incidents, setIncidents] = useState([]);
  const [search, setSearch] = useState("");

  const [form, setForm] = useState({
    title: "",
    description: "",
    severity: "High",
    service: ""
  });

  useEffect(() => {
    loadIncidents();
  }, []);

  async function loadIncidents() {
    const res = await axios.get(`${API}/incidents/`);
    setIncidents(res.data);
  }

  async function createIncident(e) {
    e.preventDefault();

    await axios.post(`${API}/incidents/`, form);

    setForm({
      title: "",
      description: "",
      severity: "High",
      service: ""
    });

    loadIncidents();
  }

  const resolveIncident = async (id) => {
    await axios.put(`${API}/incidents/${id}/resolve`);
    loadIncidents();
  };

  const deleteIncident = async (id) => {

    await axios.delete(`${API}/incidents/${id}`);

    loadIncidents();

  };
  return (
    <div className="container">

      <h1>🚨 IncidentOps Dashboard</h1>

      <form className="incident-form" onSubmit={createIncident}>

        <input
          placeholder="Incident Title"
          value={form.title}
          onChange={(e) =>
            setForm({ ...form, title: e.target.value })
          }
        />

        <input
          placeholder="Service"
          value={form.service}
          onChange={(e) =>
            setForm({ ...form, service: e.target.value })
          }
        />

        <textarea
          placeholder="Description"
          value={form.description}
          onChange={(e) =>
            setForm({ ...form, description: e.target.value })
          }
        />

        <select
          value={form.severity}
          onChange={(e) =>
            setForm({ ...form, severity: e.target.value })
          }
        >
          <option>Critical</option>
          <option>High</option>
          <option>Medium</option>
          <option>Low</option>
        </select>

        <button>Create Incident</button>

      </form>

      <div className="cards">

        <div className="card">
          <h3>Total</h3>
          <h2>{incidents.length}</h2>
        </div>

        <div className="card">
          <h3>Critical</h3>
          <h2>{incidents.filter(i => i.severity === "Critical").length}</h2>
        </div>

        <div className="card">
          <h3>Open</h3>
          <h2>{incidents.filter(i => i.status === "OPEN").length}</h2>
        </div>

      </div>
      <div className="search-box">

        <input
          type="text"
          placeholder="🔍 Search incidents..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />

      </div>
      <table>

        <thead>

          <tr>
            <th>ID</th>
            <th>Title</th>
            <th>Priority</th>
            <th>Severity</th>
            <th>Service</th>
            <th>Status</th>
            <th>Actions</th>
          </tr>

        </thead>

        <tbody>

          {incidents
            .filter((i) =>
              i.title.toLowerCase().includes(search.toLowerCase()) ||
              i.service.toLowerCase().includes(search.toLowerCase())
            )
            .map((i) => (

              <tr key={i.id}>

                <td>{i.id}</td>

                <td>{i.title}</td>

                <td>

                  <span
                    className={
                      i.priority === "P1"
                        ? "badge red"
                        : i.priority === "P2"
                          ? "badge orange"
                          : "badge yellow"
                    }
                  >
                    {i.priority}
                  </span>

                </td>

                <td>{i.severity}</td>

                <td>{i.service}</td>

                <td>

                  <span
                    className={
                      i.status === "OPEN"
                        ? "status open"
                        : "status resolved"
                    }
                  >
                    {i.status}
                  </span>

                </td>

                <td>

                  {i.status !== "RESOLVED" && (

                    <button
                      className="resolve-btn"
                      onClick={() => resolveIncident(i.id)}
                    >
                      Resolve
                    </button>

                  )}

                  <button
                    className="delete-btn"
                    onClick={() => deleteIncident(i.id)}
                  >
                    Delete
                  </button>

                </td>

              </tr>

            ))}

        </tbody>

      </table>

    </div>
  );

}

export default App;