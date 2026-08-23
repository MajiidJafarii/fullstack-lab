import {
  useAuthRegisterCreate,
} from "@/shared/api"




export function useRegisterAction(){


  const mutation =
    useAuthRegisterCreate()



  async function register(

    data: {

      username: string

      email: string

      password: string

      password_confirm: string

    }

  ){


    return mutation.mutateAsync({

      data,

    })


  }





  return {


    register,


    isPending:
      mutation.isPending,


    error:
      mutation.error,


  }


}
