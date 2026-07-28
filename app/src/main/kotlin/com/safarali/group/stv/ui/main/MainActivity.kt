package com.safarali.group.stv.ui.main

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.fragment.app.Fragment
import com.safarali.group.stv.R
import com.safarali.group.stv.databinding.ActivityMainBinding
import com.safarali.group.stv.ui.favorites.FavoritesFragment
import com.safarali.group.stv.ui.radio.RadioFragment
import com.safarali.group.stv.ui.settings.SettingsFragment
import com.safarali.group.stv.ui.tv.TvFragment

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        setSupportActionBar(binding.toolbar)
        binding.bottomNav.setOnItemSelectedListener { item ->
            when (item.itemId) {
                R.id.nav_tv -> replaceFragment(TvFragment())
                R.id.nav_radio -> replaceFragment(RadioFragment())
                R.id.nav_favorites -> replaceFragment(FavoritesFragment())
                R.id.nav_settings -> replaceFragment(SettingsFragment())
                else -> false
            }
        }
        binding.bottomNav.selectedItemId = R.id.nav_tv
    }

    private fun replaceFragment(fragment: Fragment): Boolean {
        supportFragmentManager.beginTransaction()
            .replace(R.id.fragment_container, fragment)
            .commit()
        return true
    }
}
