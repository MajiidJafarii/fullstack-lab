import {
  Moon,
  Sun,
} from "lucide-react"


import {
  useTheme,
} from "next-themes"


import {
  Button,
} from "@/shared/ui/button"



export function ThemeToggle() {


  const {
    theme,
    setTheme,
  } = useTheme()



  return (

    <Button

      variant="outline"

      size="icon"

      className="rounded-xl"

      onClick={() =>

        setTheme(
          theme === "dark"
            ? "light"
            : "dark"
        )

      }

    >

      {
        theme === "dark"
          ? <Sun size={18} />
          : <Moon size={18} />
      }


    </Button>

  )

}
