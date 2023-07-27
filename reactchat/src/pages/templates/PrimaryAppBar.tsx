import AppBar from '@mui/material/AppBar'
import Box from '@mui/material/Box'
import Toolbar from '@mui/material/Toolbar'
import MenuIcon from '@mui/icons-material/Menu'
import Link from '@mui/material/Link'
import { Drawer } from '@mui/material'

import { useTheme } from "@mui/material/styles";
import { IconButton, Typography } from '@mui/material';
import React, { useState } from 'react'
const PrimaryAppBar = () => {
    const [sideMenu, SetSideMenu] = useState(false)
    const theme = useTheme()
    // eslint-disable-next-line @typescript-eslint/no-unused-vars
    const toggleDrawer = (open: boolean) => (_event: React.MouseEvent) => {
        SetSideMenu(open)
    }

    return (
        <AppBar sx=
            {{
                zIndex: (theme) => theme.zIndex.drawer + 2,
                backgroundColor: theme.palette.background.default, borderBottom: `1px solid ${theme.palette.divider}`
            }}>
            <Toolbar variant='dense' sx={{
                height: theme.primaryAppBar.height,
                minHeight: theme.primaryAppBar.height
            }}>
                <Box sx={{ display: { xs: "block", sm: "none" } }}>
                    <IconButton color="inherit" aria-label='open drawer' edge="start" sx={{ mr: 2 }} onClick={toggleDrawer(!sideMenu)}>
                        <MenuIcon>

                        </MenuIcon>
                    </IconButton>

                </Box>
                <Drawer anchor="left" open={sideMenu}>
                    {[...Array(100)].map((_, i) => (
                        <Typography key={i} paragraph>
                            {i + 1}

                        </Typography>

                    ))}

                </Drawer>
                <Link href="/">DJCHAT</Link>

            </Toolbar>
        </AppBar >
    )
}
export default PrimaryAppBar