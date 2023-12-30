import React from 'react';
import './App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Homepage from './HomePage.tsx'

function App() {
  return (
    <>
      <div className="App">
        <BrowserRouter>
          <Routes>
            {/* <Route path='/login' element={<Loginpage />} /> */}
            <Route path='/' element={<Homepage />}>
              {/* <Route path='/projects' element={<ProjectListPage />} />
              <Route path='/project/:projectId' element={<ProjectDetailPage />} />
              <Route path='/admin-dashboard-page' element={<AdminDashboardPage />} />
              <Route path='/client-dashboard-page' element={<ClientDashboardPage />} />
              <Route path='/student-dashboard-page' element={<StudentDashboardPage />} />
              <Route path='/coordinator-dashboard-page' element={<CoordinatorDashboardPage />} />
              <Route path='/groups' element={<GroupListPage />} />
              <Route path='/courseList' element={<Course_List />} />
              <Route path='/student-profile-page' element={<StudentProfilePage />} />
              <Route path='/client-profile-page' element={<ClientProfilePage />} />
              <Route path='/coordinator-profile-page' element={<CoordinatorProfilePage />} />
              <Route path='/admin-profile-page' element={<AdminProfilePage />} />
              <Route path='/pending-profile-page' element={<PendingProfilePage />} />
              <Route path='/tutor-dashboard-page' element={<TutorDashboardPage />} />
              <Route path='/tutor-profile-page' element={<TutorProfilePage />} /> */}
            </Route>

          </Routes>
        </BrowserRouter>
      </div>
    </>
  );
}

export default App;
