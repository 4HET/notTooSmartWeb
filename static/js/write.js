function write_to_session(fileName, fileId) {
    localStorage.clear();
    return (fileName, fileId);
    localStorage.setItem('fileName', fileName);
    localStorage.setItem('fileId', fileId);
}