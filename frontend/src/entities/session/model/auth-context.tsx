import {
  createContext,
  useContext,
  useEffect,
  useState,
} from "react"


import {
  api,
} from "@/shared/api"


import type {
  User,
} from "@/entities/session"





type AuthContextType = {

  authenticated: boolean

  loading: boolean

  user: User | null

  refresh: () => Promise<void>

  loginSuccess: () => Promise<void>

  logout: () => Promise<void>

}





const AuthContext =
  createContext<AuthContextType | null>(null)





export function AuthProvider({

  children,

}: {

  children: React.ReactNode

}) {



  const [
    authenticated,
    setAuthenticated,
  ] = useState(false)



  const [
    user,
    setUser,
  ] = useState<User | null>(null)



  const [
    loading,
    setLoading,
  ] = useState(true)







  async function refresh() {


    try {


      const response =
        await api.get<User>(
          "/api/me/"
        )



      setUser(
        response.data
      )


      setAuthenticated(true)



    } catch {


      setUser(null)


      setAuthenticated(false)


    }


  }







  useEffect(() => {


    refresh()

      .finally(() => {

        setLoading(false)

      })


  }, [])







  async function loginSuccess() {


    await refresh()


  }







  async function logout() {


    try {


      await api.post(
        "/api/auth/logout/"
      )


    } catch {


    } finally {


      setUser(null)


      setAuthenticated(false)


    }


  }







  return (

    <AuthContext.Provider

      value={{

        authenticated,

        loading,

        user,

        refresh,

        loginSuccess,

        logout,

      }}

    >

      {children}

    </AuthContext.Provider>

  )

}







export function useAuth() {


  const context =
    useContext(AuthContext)



  if (!context) {


    throw new Error(
      "useAuth must be used inside AuthProvider"
    )


  }



  return context


}
