import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.jsx';
import './assets/scss/style.scss';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import Home from './pages/Home.jsx';
import CodeAssistance from './pages/CodeAssistance.jsx';
import Knowledge from './pages/Knowledge.jsx';

const Error = () => <div>Page not found</div>;

const router = createBrowserRouter([
  {
    path: '/',
    element: <App />,
    errorElement: <Error />,
    children: [
      {
        path: '/',
        element: <Home />,
      },
      {
        path: 'codeAssistance',
        element: <CodeAssistance />,
      },
      {
        path: 'knowledge',
        element: <Knowledge />
      },
    ],
  },
]);

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
);
