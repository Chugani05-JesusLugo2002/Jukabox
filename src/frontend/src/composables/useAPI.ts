export const useAPI = () => {
  async function getData(path: string): Promise<any> {
    const url = 'http://localhost:8000/api/v1/' + path
    try {
      const response = await fetch(url)
      const data = await response.json()
      return data
    } catch (error) {
      console.error(error)
    }
  }

  return { getData }
}
