import React, { useState } from 'react';

const FileUpload = () => {
  const [file, setFile] = useState(null);
  const [uploadStatus, setUploadStatus] = useState('');
  
  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!file) {
      setUploadStatus('No file selected.');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    fetch('http://localhost:8000/upload/', {
      method: 'POST',
      body: formData,
    })
      .then((response) => {
        if (response.ok) {
          setUploadStatus('File uploaded successfully!');
        } else {
          setUploadStatus('Failed to upload file. Please try again.');
        }
      })
      .catch((error) => {
        setUploadStatus(`Error: ${error.message}`);
      });
  };

  return (
    <div>
      <h2>Upload CSV File</h2>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} />
        <button type="submit">Upload</button>
      </form>
      {uploadStatus && <p>{uploadStatus}</p>}
    </div>
  );
};

export default FileUpload;