import {
  createContext,
  useContext,
  useEffect,
  useState,
} from "react"


import {
  api,
} from "@/shared/api"



type AuthContextType = {

  authenticated: boolean

  loading: boolean

  refresh: () => Promise<void>

  loginSuccess: () => void

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
    loading,
    setLoading,
  ] = useState(true)



  async function refresh() {

    try {


      await api.get(
        "/api/me/"
      )


      setAuthenticated(true)


    } catch {


      setAuthenticated(false)


    }

  }




  useEffect(() => {


    refresh()
      .finally(() => {

        setLoading(false)

      })


  }, [])




  function loginSuccess() {


    setAuthenticated(true)


  }





  async function logout() {


    try {


      await api.post(
        "/api/auth/logout/"
      )


    } catch {


      // حتی اگر API خطا داد
      // سمت فرانت خروج انجام شود


    } finally {


      setAuthenticated(false)


    }


  }





  return (

    <AuthContext.Provider

      value={{

        authenticated,

        loading,

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
