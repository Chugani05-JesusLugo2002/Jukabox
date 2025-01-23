async function getJsonData(path: string): Promise<any> {
  try {
    const response = await fetch(path)
    const data = await response.json()
    return data
  } catch (error) {
    console.error('Something goes wrong using getJsonData function!', error)
  }
}

export { getJsonData }
