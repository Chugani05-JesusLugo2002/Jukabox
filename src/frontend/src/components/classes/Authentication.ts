export interface User {
  id: number
  token: string
  username: string
  first_name: string
  last_name: string
  email: string
  avatar: string
}

export interface SignupData {
  username: string
  first_name: string
  last_name: string
  email: string
  password: string
}

export interface LoginData {
  username: string
  password: string
}
